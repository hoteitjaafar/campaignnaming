import streamlit as st
import pandas as pd
import numpy as np


st.title("Campaign Naming Application")
st.title("")

col1, col2 = st.columns(2)
brand = col1.selectbox(
     'Brand Title:',
     ('Dabur', 'RT', 'Abbott', 'NullBrand')
     )
sub_brand = col2.selectbox(
    'Sub-Brand Title:',
    ('Amla', 'Vatika', 'NullSubBrand')
    )


col2, col3 = st.columns(2)
market = col2.selectbox(
    'Target Market:',
    ('UAE', 'KSA', 'KW', 'QA', 'OM', 'BH', 'NullMarket')
)
placement = col3.selectbox(
    'Advertising Media Platform:',
    ('FBIG', 'IG', 'FB', 'GDN', 'Search', 'YouTube', 'Snapchat', 'TikTok', 'LinkedIn', 'Yahoo', 'Speakol', 'Teads', 'NullPlatform')
)


col4, col5 = st.columns(2)
objective = col4.selectbox(
    'Campaign Objective:',
    ('CPMR', 'CPM', 'CPC', 'CPV', 'CPL', 'CPA', 'CPLPV', 'NullObjective')
)
special_offer = col5.selectbox(
    'Special Offer Title:',
    ('SpecialOffer', 'NullOffer')
)


col6, col7 = st.columns(2)
language = col6.selectbox(
    'Target Language:',
    ('En', 'Ar', 'NullLanguage')
)
gender = col7.selectbox(
    'Target Gender:',
    ('Male', 'Female', 'NullGender')
)


col8, col9 = st.columns(2)
age = col8.selectbox(
    'Target Age:',
    ('18to24', '25to34', 'NullAge')
)
format = col9.selectbox(
    'Ad Format:',
    ('StaticImage', 'Video', 'Carousel', 'Catalog', 'ResponsiveAd', 
    'ExpendedAd', 'GmailAd', 'DiscoveryAd', 'HTML5', 'StaticDisplay(GDN)', 'NullAdFormat')
)


col10, col11 = st.columns(2)
year = col10.selectbox(
    'Campaign Initiation Year:',
    ('2022', 'NullYear')
)
month = col11.selectbox(
    'Campaign Initiation Month:',
    ('January', 'February', 'March', 'April', 'May',
    'June', 'July', 'August', 'September', 'October', 
    'Novement', 'December', 'NullMonth')
)




# Coding Sheme

# Brand Coding
if brand == 'Dabur':
    coded_brand = brand.replace('Dabur', 'B1')
elif brand == 'RT':
    coded_brand = brand.replace('RT', 'B2')
elif brand == 'Abbott':
    coded_brand = brand.replace('Abbott', 'B3')
else:
    coded_brand = brand.replace('NullBrand', 'B0')

# Sub-Brand Coding
if sub_brand == 'Vatika':
    coded_sub_brand = sub_brand.replace('Vatika', 'SB1')
elif sub_brand == 'Amla':
    coded_sub_brand = sub_brand.replace('Amla', 'SB2')
else:
    coded_sub_brand = sub_brand.replace('NullSubBrand', 'SB0')

# Market Coding
if market == 'UAE':
    coded_market = market.replace('UAE', 'M1')
elif market == 'KSA':
    coded_market = market.replace('KSA', 'M2')
elif market == 'KW':
    coded_market = market.replace('KW', 'M3')
elif market == 'QA':
    coded_market = market.replace('QA', 'M4')
elif market == 'OM':
    coded_market = market.replace('OM', 'M5')
elif market == 'BH':
    coded_market = market.replace('BH', 'M6')
else:
    coded_market = market.replace('NullMarket', 'M0')

# Placement Coding
if placement == 'FBIG':
    coded_placement = placement.replace('FBIG', 'P1')
elif placement == 'IG':
    coded_placement = placement.replace('IG', 'P2')
elif placement == 'FB':
    coded_placement = placement.replace('FB', 'P3')
elif placement == 'GDN':
    coded_placement = placement.replace('GDN', 'P4')
elif placement == 'Search':
    coded_placement = placement.replace('Search', 'P5')
elif placement == 'YouTube':
    coded_placement = placement.replace('YouTube', 'P6')
elif placement == 'Snapchat':
    coded_placement = placement.replace('Snapchat', 'P7')
elif placement == 'TikTok':
    coded_placement = placement.replace('TikTok', 'P8')
elif placement == 'LinkedIn':
    coded_placement = placement.replace('LinkedIn', 'P9')
elif placement == 'Yahoo':
    coded_placement = placement.replace('Yahoo', 'P10')
elif placement == 'Speakol':
    coded_placement = placement.replace('Speakol', 'P11')
elif placement == 'Teads':
    coded_placement = placement.replace('Teads', 'P12')
else:
    coded_placement = placement.replace('NullPlatform', 'P0')

# Objective Coding
if objective == 'CPMR':
    coded_objective = objective.replace('CPMR', 'O1')
elif objective == 'CPM':
    coded_objective = objective.replace('CPM', 'O2')
elif objective == 'CPC':
    coded_objective = objective.replace('CPC', 'O3')
elif objective == 'CPV':
    coded_objective = objective.replace('CPV', 'O4')
elif objective == 'CPL':
    coded_objective = objective.replace('CPL', 'O5')
elif objective == 'CPA':
    coded_objective = objective.replace('CPA', 'O6')
elif objective == 'CPLPV':
    coded_objective = objective.replace('CPLPV', 'O7')
else:
    coded_objective = objective.replace('NullObjective', 'O0')

# Special Offer Coding
if special_offer == 'SpecialOffer':
    coded_special_offer = special_offer.replace('SpecialOffer', 'SO1')
else:
    coded_special_offer = special_offer.replace('NullOffer', 'SO0')

# Langauge Coding
if language == 'En':
    coded_language = language.replace('En', 'L1')
elif language == 'Ar':
    coded_language = language.replace('Ar', 'L2')
else:
    coded_language = language.replace('NullLanguage', 'L0')

# Gender Coding:
if gender == 'Male':
    coded_gender = gender.replace('Male', 'G1')
elif gender == 'Female':
    coded_gender = gender.replace('Female', 'G2')
else:
    coded_gender = gender.replace('NullGender', 'G0')

# Age Coding
if age == '18to24':
    coded_age = age.replace('18to24', 'A1')
elif age == '25to34':
    coded_age = age.replace('25to34', 'A2')
else:
    coded_age = age.replace('NullAge', 'A0')

# Format Coding
if format == 'StaticImage':
    coded_format = format.replace('StaticImage', 'F1')
elif format == 'Video':
    coded_format = format.replace('Video', 'F2')
elif format == 'Carousel':
    coded_format = format.replace('Carousel', 'F3')
elif format == 'Catalog':
    coded_format = format.replace('Catalog', 'F4')
elif format == 'ResponsiveAd':
    coded_format = format.replace('ResponsiveAd', 'F5')
elif format == 'ExpendedAd':
    coded_format = format.replace('ExpendedAd', 'F6')
elif format == 'GmailAd':
    coded_format = format.replace('GmailAd', 'F7')
elif format == 'DiscoveryAd':
    coded_format = format.replace('DiscoveryAd', 'F8')
elif format == 'HTML5':
    coded_format = format.replace('HTML5', 'F9')
elif format == 'StaticDisplay(GDN)':
    coded_format = format.replace('StaticDisplay(GDN)', 'F10')
else:
    coded_format = format.replace('NullAdFormat', 'F0')

# Month Coding
if month == 'January':
    coded_month = month.replace('January', 'MO1')
elif month == 'Febrauary':
    coded_month = month.replace('February', 'MO2')
elif month == 'March':
    coded_month = month.replace('March', 'MO3')
elif month == 'April':
    coded_month = month.replace('April', 'MO4')
elif month == 'May':
    coded_month = month.replace('May', 'MO5')
elif month == 'June':
    coded_month = month.replace('June', 'MO6')
elif month == 'July':
    coded_month = month.replace('July', 'MO7')
elif month == 'August':
    coded_month = month.replace('August', 'MO8')
elif month == 'September':
    coded_month = month.replace('September', 'MO9')
elif month == 'October':
    coded_month = month.replace('October', 'MO10')
elif month == 'November':
    coded_month = month.replace('November', 'MO11')
elif month == 'December':
    coded_month = month.replace('December', 'MO12')
else:
    coded_month = month.replace('NullMonth', 'MO0')





# Campaign, Adset, and Ad names creation
st.title('')
st.title('')


campaign_name = (brand + '_' + sub_brand + '_' + market + '_' + placement + 
                    '_' + objective + '_' + year + '_' + month)
adset_name = (brand + '_' + sub_brand + '_' + market + '_' + placement + 
                    '_' + objective + '_' + language + '_' + 
                    gender + '_' + age + '_' + year + '_' + month)
ad_name = (brand + '_' + sub_brand + '_' + market + '_' + placement + 
                    '_' + objective + '_' + special_offer + '_' + language + '_' + 
                    gender + '_' + age + '_' + format + '_' + year + '_' + month)



coded_campaign_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_market + '_' + coded_placement + 
                    '_' + coded_objective + '_' + year + '_' + coded_month)
coded_adset_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_market + '_' + coded_placement + 
                    '_' + coded_objective + '_' + coded_language + '_' + 
                    coded_gender + '_' + coded_age + '_' + year + '_' + coded_month)
coded_ad_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_market + '_' + coded_placement + 
                    '_' + coded_objective + '_' + coded_special_offer + '_' + coded_language + '_' + 
                    coded_gender + '_' + coded_age + '_' + coded_format + '_' + year + '_' + coded_month)



st.subheader('Campaign Name:')
st.write('Full Campaign Name:')
st.code(campaign_name)
st.write('Coded Campaign Name (Required):')
st.code(coded_campaign_name)

st.title('')

st.subheader('Adset Name:')
st.write('Full Adset Name:')
st.code(adset_name)
st.write('Coded Adset Name (Required):')
st.code(coded_adset_name)


st.title('')

st.subheader('Ad Name:')
st.write('Full Ad name:')
st.code(ad_name)
st.write('Coded Ad Name (Required):')
st.code(coded_ad_name)
