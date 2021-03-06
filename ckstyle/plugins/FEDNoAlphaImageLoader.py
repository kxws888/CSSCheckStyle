from Base import *

class FEDNoAlphaImageLoader(RuleChecker):
    def __init__(self):
        self.id = 'no-alpha-image-loader'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'should not use AlphaImageLoader in "${selector}"'

    def check(self, rule):
        if rule.value.find('AlphaImageLoader') != -1:
            return False
        return True 
