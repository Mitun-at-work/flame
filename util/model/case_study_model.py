from dataclasses import dataclass

@dataclass
class CaseStudy :
    title : str
    description : str
    created_on : str
    updated_on : str
    case_study_id : int
    
    monthly_img_address : str
    monthly_trend : str

    weekly_img_address : str
    weekly_trend : str

    daily_img_address : str
    daily_trend : str

    dxy_img_address : str
    dxy_trend : str
