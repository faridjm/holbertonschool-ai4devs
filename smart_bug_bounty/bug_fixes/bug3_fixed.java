class Bug3 {
    static double averageScore(int[] scores) {
        if (scores.length == 0) {
            throw new IllegalArgumentException("At least one score is required.");
        }

        long total = 0;
        for (int score : scores) {
            total += score;
        }

        return (double) total / scores.length;
    }

    public static void main(String[] args) {
        int[] scores = {8, 9};
        System.out.println(averageScore(scores));
    }
}
