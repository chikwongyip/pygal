from pygal_maps_world import i18n as world

def get_country_code(country_name):
    """根据国家名称返回国别码"""
    for code,name in world.COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有返回 None
    return None
