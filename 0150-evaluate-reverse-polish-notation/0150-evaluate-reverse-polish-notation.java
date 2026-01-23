class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String str : tokens) {
            if(str.equals("+") || str.equals("-") || str.equals("*") || str.equals("/")) {
                int num1 = stack.pop();
                int num2 = stack.pop();
                if(str.equals("+")) {
                    stack.push(num1 + num2);
                } else if(str.equals("-")) {
                    stack.push(num2 - num1);
                } else if(str.equals("*")) {
                    stack.push(num1 * num2);
                } else {
                    stack.push((int) num2 / num1);
                } 
            }
            else {
                stack.push(Integer.valueOf(str));
            }
        }

        return stack.pop();
    }
}