class Solution {
    public int bitwiseComplement(int n) {
        StringBuilder result = new StringBuilder();
        String binary = Integer.toBinaryString(n);
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                result.append("0");
            } else if (binary.charAt(i) == '0') {
                result.append("1");
            }
        }
        return Integer.parseInt(result.toString(), 2);
    }
}