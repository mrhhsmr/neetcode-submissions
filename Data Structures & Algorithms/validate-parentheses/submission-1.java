class Solution {
    public boolean isValid(String s) {
        var stack = new Stack<Character>();
        for(int i = 0; i < s.length(); i ++){
            if(s.charAt(i) == ')'){
                if(stack.size() == 0 || stack.pop() != '('){
                    return false;
                }
            }
            if(s.charAt(i) == ']'){
                if(stack.size() == 0 || stack.pop() != '['){
                    return false;
                }
            }
            if(s.charAt(i) == '}'){
                if(stack.size() == 0 || stack.pop() != '{'){
                    return false;
                }
            }

            if(s.charAt(i) == '{' || s.charAt(i) == '(' || s.charAt(i) == '['){
                stack.push(s.charAt(i));
            }
            
        }

        return stack.size() == 0;
    }
}
