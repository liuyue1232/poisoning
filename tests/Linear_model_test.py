from poisoning.xiao2018.equations import equation2, equation7
import sklearn.linear_model as LM
import pytest

class Test_Equation_2:
    
    okay_X = [[1, 2], [3, 4]]
    okay_Y = [1, 2]
    okay_lambda = 0.23
    
    def test_invalid_parameters(self):
        
        with pytest.raises(TypeError) as info:
            equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, this=3)        
    
        with pytest.raises(TypeError) as info:
            equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, other='haha')
    
    def test_invalid_type(self):
        
        with pytest.raises(TypeError) as info:
            equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, type='not allowed')
    
        with pytest.raises(TypeError) as info:
            equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, other='elastic net')
            
    def test_invalid_dimensions(self):
        
        with pytest.raises(ValueError) as info:
            equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y + [3])
            
    def test_lasso(self):
        
        res = equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, type='lasso')
        accurate = LM.Lasso().fit(Test_Equation_2.okay_X, Test_Equation_2.okay_Y)
        accurate = (accurate.coef_, accurate.intercept_)
        
        assert all([r == a for (r, a) in zip(res[0], accurate[0])])
        assert res[1], accurate[1]
        
    def test_ridge(self):
            
        res = equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, type='ridge')
        accurate = LM.Ridge().fit(Test_Equation_2.okay_X, Test_Equation_2.okay_Y)
        accurate = (accurate.coef_, accurate.intercept_)
        
        assert all([r == a for (r, a) in zip(res[0], accurate[0])])
        assert res[1], accurate[1]
    
    def test_elastic(self):
            
        res = equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, type='elastic')
        accurate = LM.ElasticNet().fit(Test_Equation_2.okay_X, Test_Equation_2.okay_Y)
        accurate = (accurate.coef_, accurate.intercept_)
        
        assert all([r == a for (r, a) in zip(res[0], accurate[0])])
        assert res[1], accurate[1]
        
    def test_lasso_lambda(self):
        
        res = equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, type='lasso', alpha=Test_Equation_2.okay_lambda)
        accurate = LM.Lasso(alpha=Test_Equation_2.okay_lambda).fit(Test_Equation_2.okay_X, Test_Equation_2.okay_Y)
        accurate = (accurate.coef_, accurate.intercept_)
        
        assert all([r == a for (r, a) in zip(res[0], accurate[0])])
        assert res[1], accurate[1]
        
    def test_ridge_lambda(self):
            
        res = equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, type='ridge', alpha=Test_Equation_2.okay_lambda)
        accurate = LM.Ridge(alpha=Test_Equation_2.okay_lambda).fit(Test_Equation_2.okay_X, Test_Equation_2.okay_Y)
        accurate = (accurate.coef_, accurate.intercept_)
        
        assert all([r == a for (r, a) in zip(res[0], accurate[0])])
        assert res[1], accurate[1]
    
    def test_elastic_lambda(self):
            
        res = equation2(Test_Equation_2.okay_X, Test_Equation_2.okay_Y, type='elastic', alpha=Test_Equation_2.okay_lambda)
        accurate = LM.ElasticNet(alpha=Test_Equation_2.okay_lambda).fit(Test_Equation_2.okay_X, Test_Equation_2.okay_Y)
        accurate = (accurate.coef_, accurate.intercept_)
        
        assert all([r == a for (r, a) in zip(res[0], accurate[0])])
        assert res[1], accurate[1]

        
class Test_Equation_7:
    
    okay_X = [[1, 2], [3, 4]]
    okay_Y = [1, 2]
    okay_weights = [0.2, 1.3]
    okay_biases = 0.1
    okay_lambda = 0.23
    
    def test_invalid_parameters(self):
        
        with pytest.raises(TypeError) as info:
            equation7(Test_Equation_7.okay_X, Test_Equation_7.okay_Y, Test_Equation_7.okay_weights, Test_Equation_7.okay_biases, this=3)        
    
        with pytest.raises(TypeError) as info:
            equation7(Test_Equation_7.okay_X, Test_Equation_7.okay_Y, Test_Equation_7.okay_weights, Test_Equation_7.okay_biases, other='haha')
    
    def test_invalid_type(self):
        
        with pytest.raises(TypeError) as info:
            equation7(Test_Equation_7.okay_X, Test_Equation_7.okay_Y, Test_Equation_7.okay_weights, Test_Equation_7.okay_biases, type='not allowed')
    
        with pytest.raises(TypeError) as info:
            equation7(Test_Equation_7.okay_X, Test_Equation_7.okay_Y, Test_Equation_7.okay_weights, Test_Equation_7.okay_biases, other='elastic net')
            
    def test_invalid_dimensions(self):
        
        with pytest.raises(ValueError) as info:
            equation7(Test_Equation_7.okay_X, Test_Equation_7.okay_Y  + [3], Test_Equation_7.okay_weights, Test_Equation_7.okay_biases)
            
        with pytest.raises(ValueError) as info:
            equation7(Test_Equation_7.okay_X, Test_Equation_7.okay_Y  + [3], Test_Equation_7.okay_weights + [3], Test_Equation_7.okay_biases)