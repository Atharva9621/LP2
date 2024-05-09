public class CalculatorController {
    public Integer num1 { get; set; }
    public Integer num2 { get; set; }
    public Integer addResult { get; set; }
    public Integer subtractResult { get; set; }
    public Integer multiplyResult { get; set; }
    public Boolean showResult { get; set; }

    public CalculatorController() {
        num1 = 0;
        num2 = 0;
        addResult = 0;
        subtractResult = 0;
        multiplyResult = 0;
        showResult = false;
    }

    public void performAdd() {
        addResult = Calculator.add(num1, num2);
        showResult = true;
    }

    public void performSubtract() {
        subtractResult = Calculator.subtract(num1, num2);
        showResult = true;
    }

    public void performMultiply() {
        multiplyResult = Calculator.multiply(num1, num2);
        showResult = true;
    }
}