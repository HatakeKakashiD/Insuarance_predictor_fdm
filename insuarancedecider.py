def get_insurance_types(income_category, age, workclass):
    # Define insurance categories based on income, age, and workclass
    insurance_data = {
        '>50K': {
            (0, 17): {
                'Private Sector Employee': ['Not Suitable for Insurance'],
                'Self-Employed (Not Incorporated)': ['Not Suitable for Insurance'],
                'Self-Employed (Incorporated)': ['Not Suitable for Insurance'],
                'Federal Government Employee': ['Not Suitable for Insurance'],
                'Local Government Employee': ['Not Suitable for Insurance'],
                'State Government Employee': ['Not Suitable for Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            },
            (18, 30): {
                'Private Sector Employee': ['Comprehensive Health Insurance', 'Comprehensive Life Insurance'],
                'Self-Employed (Not Incorporated)': ['Comprehensive Health Insurance', 'Comprehensive Life Insurance'],
                'Self-Employed (Incorporated)': ['Comprehensive Health Insurance', 'Comprehensive Life Insurance'],
                'Federal Government Employee': ['Comprehensive Health Insurance', 'Comprehensive Life Insurance'],
                'Local Government Employee': ['Comprehensive Health Insurance', 'Comprehensive Life Insurance'],
                'State Government Employee': ['Comprehensive Health Insurance', 'Comprehensive Life Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            },
            (31, 55): {
                'Private Sector Employee': ['Comprehensive Health Insurance', 'Premium Family Health Insurance',
                                            'Comprehensive Life Insurance', 'Income Protection Insurance'],
                'Self-Employed (Not Incorporated)': ['Comprehensive Health Insurance',
                                                     'Premium Family Health Insurance',
                                                     'Comprehensive Life Insurance', 'Disability Insurance',
                                                     'Income Protection Insurance'],
                'Self-Employed (Incorporated)': ['Comprehensive Health Insurance', 'Premium Family Health Insurance',
                                                 'Comprehensive Life Insurance', 'Disability Insurance',
                                                 'Income Protection Insurance'],
                'Federal Government Employee': ['Comprehensive Health Insurance', 'Premium Family Health Insurance',
                                                'Comprehensive Life Insurance'],
                'Local Government Employee': ['Comprehensive Health Insurance', 'Premium Family Health Insurance',
                                              'Comprehensive Life Insurance'],
                'State Government Employee': ['Comprehensive Health Insurance', 'Premium Family Health Insurance',
                                              'Comprehensive Life Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            },
            (55, 100): {
                'Private Sector Employee': ['Retirement Plans', 'Investment Insurance',
                                            'Comprehensive Life Insurance', 'Accident Insurance',
                                            'Disability Insurance'],
                'Self-Employed (Not Incorporated)': ['Retirement Plans', 'Investment Insurance',
                                                     'Comprehensive Life Insurance', 'Accident Insurance',
                                                     'Disability Insurance'],
                'Self-Employed (Incorporated)': ['Retirement Plans', 'Investment Insurance',
                                                 'Comprehensive Life Insurance', 'Accident Insurance',
                                                 'Disability Insurance'],
                'Federal Government Employee': ['Retirement Plans', 'Comprehensive Life Insurance',
                                                'Disability Insurance'],
                'Local Government Employee': ['Retirement Plans', 'Comprehensive Life Insurance',
                                              'Disability Insurance'],
                'State Government Employee': ['Retirement Plans', 'Comprehensive Life Insurance',
                                              'Disability Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            }
        },
        '<=50K': {
            (0, 17): {
                'Private Sector Employee': ['Not Suitable for Insurance'],
                'Self-Employed (Not Incorporated)': ['Not Suitable for Insurance'],
                'Self-Employed (Incorporated)': ['Not Suitable for Insurance'],
                'Federal Government Employee': ['Not Suitable for Insurance'],
                'Local Government Employee': ['Not Suitable for Insurance'],
                'State Government Employee': ['Not Suitable for Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            },
            (18, 30): {
                'Private Sector Employee': ['Basic Health Insurance', 'Basic Life Insurance',
                                            'Educational Support Insurance'],
                'Self-Employed (Not Incorporated)': ['Basic Health Insurance', 'Basic Life Insurance',
                                                     'Educational Support Insurance'],
                'Self-Employed (Incorporated)': ['Basic Health Insurance', 'Basic Life Insurance',
                                                 'Educational Support Insurance'],
                'Federal Government Employee': ['Basic Health Insurance', 'Basic Life Insurance'],
                'Local Government Employee': ['Basic Health Insurance', 'Basic Life Insurance'],
                'State Government Employee': ['Basic Health Insurance', 'Basic Life Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            },
            (31, 55): {
                'Private Sector Employee': ['Basic Health Insurance', 'Affordable Family Health Insurance',
                                            'Family Health Insurance', 'Life Insurance'],
                'Self-Employed (Not Incorporated)': ['Basic Health Insurance', 'Affordable Family Health Insurance',
                                                     'Family Health Insurance', 'Life Insurance'],
                'Self-Employed (Incorporated)': ['Basic Health Insurance', 'Affordable Family Health Insurance',
                                                 'Family Health Insurance', 'Life Insurance'],
                'Federal Government Employee': ['Basic Health Insurance', 'Family Health Insurance', 'Life Insurance'],
                'Local Government Employee': ['Basic Health Insurance', 'Family Health Insurance', 'Life Insurance'],
                'State Government Employee': ['Basic Health Insurance', 'Family Health Insurance', 'Life Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            },
            (55, 100): {
                'Private Sector Employee': ['Affordable Family Health Insurance', 'Family Health Insurance',
                                            'Basic Life Insurance', 'Educational Insurance'],
                'Self-Employed (Not Incorporated)': ['Affordable Family Health Insurance', 'Family Health Insurance',
                                                     'Basic Life Insurance', 'Educational Insurance'],
                'Self-Employed (Incorporated)': ['Affordable Family Health Insurance', 'Family Health Insurance',
                                                 'Basic Life Insurance', 'Educational Insurance'],
                'Federal Government Employee': ['Affordable Family Health Insurance', 'Family Health Insurance',
                                                'Basic Life Insurance', 'Educational Insurance'],
                'Local Government Employee': ['Affordable Family Health Insurance', 'Family Health Insurance',
                                              'Basic Life Insurance', 'Educational Insurance'],
                'State Government Employee': ['Affordable Family Health Insurance', 'Family Health Insurance',
                                              'Basic Life Insurance', 'Educational Insurance'],
                'Unpaid Worker': ['Not Suitable for Insurance'],
                'Never Worked': ['Not Suitable for Insurance']
            }
        }
    }

    # Determine the age range
    if age < 18:
        age_range = (0, 17)
    elif 18 <= age <= 30:
        age_range = (18, 30)
    elif 31 <= age <= 55:
        age_range = (31, 55)
    else:
        age_range = (55, 100)

    # Get insurance types
    insurance_types = insurance_data[income_category].get(age_range, {}).get(workclass, ['No Matching Insurance Types'])

    # Format insurance types in bullet format
    bullet_output = ''.join(f"- {insurance}" for insurance in insurance_types)

    return bullet_output


# Example usage
print(get_insurance_types('>50K', 2, 'Private Sector Employee'))
print(get_insurance_types('<=50K', 45, 'Self-Employed (Not Incorporated)'))
print(get_insurance_types('<=50K', 65, 'Unpaid Worker'))
