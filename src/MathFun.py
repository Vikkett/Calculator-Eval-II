class MathFun:

    @classmethod
    def execute(cls, math_request):
        operator = math_request.get_operator()
        ope1 = math_request.get_ope1()
        ope2 = math_request.get_ope2()

        match operator:
            case 'max':
                if ope1 == ope2:
                    return EqualityException("Both operands are equal")
                return max(ope1, ope2)
            case 'is_sum_even':
                raise NotImplementedError
            case _:
                raise NotImplementedError

class MathFunException(Exception):
    pass

class FunOperatorNotSupportedException(MathFunException):
    pass

class EqualityException(MathFunException):
    pass