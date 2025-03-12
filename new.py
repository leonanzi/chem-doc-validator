# 基础化学式校验
def validate_formula(formula):
    elements = re.findall('[A-Z][a-z]?\d*', formula)
    return all([is_valid_element(e) for e in elements])
