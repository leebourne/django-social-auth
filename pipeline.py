from django.shortcuts import redirect
from social.pipeline.partial import partial
from .models import (
    Company,
    Employee,
)   

import logging
logger = logging.getLogger(__name__)

@partial
def require_company(strategy, details, user=None, is_new=False, *args, **kwargs):
    '''
    Check if there is an employee record with the email address supplied by the social website
    '''
    logger.info('require_company')

    email = details.get('email')
    if email:
        logger.info('Checking %s',email)
        employee = Employee.objects.filter(email=email,active=True).first()
        if not employee is None and employee.company:
            logger.info('Success for %s',email)
            return
        logger.info('No invite for %s',email)
        
    if not details.get('company_name'):
        logger.info("Company name supplied")
        company_name = strategy.request_data().get('company_name')
        if company_name:
            details['company_name'] = company_name
        else:
            return redirect('/require_company')

def associate_user(backend, user, details, response, is_new=False, *args, **kwargs):
    '''
    Associate Company, Employee and Social User records
    New user and company:
      - Create the company
      - Create the employee
      - Associate the social user with the employee
    New user, existing company
      - Associate the social user with the employee
    '''
    logger.info('associate_user')
    if not is_new:
        return

    # If company name has been supplied then create both a Company and an Employee record
    if details.get('company_name'):
        logger.info('new company and employee')
        try:
            company = Company(company_name=details['company_name'])
            company.save()
            employee = Employee(email=user.email,
                                company=company)
        except:
            logger.info('Error creating company and user')
    else:
        logger.info('invited employee')
        employee = Employee.objects.filter(email=user.email,active=True).first()
        if not employee:
            logger.info('Employee %s not found',user.email)
            return redirect('/require_company')
            
    employee.user = user
    employee.save()