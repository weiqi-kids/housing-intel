"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .asia_cement import AsiaCementFetcher
from .caterpillar import CaterpillarFetcher
from .cathay_real_estate import CathayRealEstateFetcher
from .chong_hong import ChongHongFetcher
from .crh import CrhFetcher
from .daiwa_house import DaiwaHouseFetcher
from .dr_horton import DrHortonFetcher
from .farglory import FargloryFetcher
from .highwealth import HighwealthFetcher
from .huaku import HuakuFetcher
from .huang_hsiang import HuangHsiangFetcher
from .kb_home import KbHomeFetcher
from .kindom import KindomFetcher
from .lennar import LennarFetcher
from .nippon_steel import NipponSteelFetcher
from .nvr import NvrFetcher
from .pultegroup import PultegroupFetcher
from .ruentex import RuentexFetcher
from .saint_gobain import SaintGobainFetcher
from .san_yuan import SanYuanFetcher
from .sekisui_house import SekisuiHouseFetcher
from .sumitomo_forestry import SumitomoForestryFetcher
from .taiwan_cement import TaiwanCementFetcher
from .taiwan_glass import TaiwanGlassFetcher
from .toll_brothers import TollBrothersFetcher
from .tung_ho_steel import TungHoSteelFetcher
from .vulcan_materials import VulcanMaterialsFetcher

FETCHERS = {
    "asia_cement": AsiaCementFetcher,
    "caterpillar": CaterpillarFetcher,
    "cathay_real_estate": CathayRealEstateFetcher,
    "chong_hong": ChongHongFetcher,
    "crh": CrhFetcher,
    "daiwa_house": DaiwaHouseFetcher,
    "dr_horton": DrHortonFetcher,
    "farglory": FargloryFetcher,
    "highwealth": HighwealthFetcher,
    "huaku": HuakuFetcher,
    "huang_hsiang": HuangHsiangFetcher,
    "kb_home": KbHomeFetcher,
    "kindom": KindomFetcher,
    "lennar": LennarFetcher,
    "nippon_steel": NipponSteelFetcher,
    "nvr": NvrFetcher,
    "pultegroup": PultegroupFetcher,
    "ruentex": RuentexFetcher,
    "saint_gobain": SaintGobainFetcher,
    "san_yuan": SanYuanFetcher,
    "sekisui_house": SekisuiHouseFetcher,
    "sumitomo_forestry": SumitomoForestryFetcher,
    "taiwan_cement": TaiwanCementFetcher,
    "taiwan_glass": TaiwanGlassFetcher,
    "toll_brothers": TollBrothersFetcher,
    "tung_ho_steel": TungHoSteelFetcher,
    "vulcan_materials": VulcanMaterialsFetcher,
}
