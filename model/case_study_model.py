from dataclasses import dataclass
from io import BytesIO

@dataclass
class CaseStudyModel :
    title : str
    notes : str
    case_study : str
    image_byte : BytesIO
    date : str
    time : str