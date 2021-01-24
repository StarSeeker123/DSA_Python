class ThreeWayPartition {
    public static void getPartition(int[] arr, int lowValue, int highValue) {
        int n = arr.length;

        int startingValue = 0, endingValue = n - 1;

        for (int i = 0; i <= endingValue;) {
            if (arr[i] < lowValue) {

                int temp = arr[startingValue];
                arr[startingValue] = arr[i];
                arr[i] = temp;
                startingValue++;
                i++;
            } else if (arr[i] > highValue) {

                int temp = arr[endingValue];
                arr[endingValue] = arr[i];
                arr[i] = temp;
                endingValue--;
            } else
                i++;
        }
    }

    public static void main(String[] args) {
        int arr[] = { 2, 5, 87, 56, 12, 4, 9, 23, 76, 1, 45 };

        getPartition(arr, 15, 30);

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");

        }
    }
}