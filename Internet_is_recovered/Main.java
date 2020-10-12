package com.company;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int quantity = sc.nextInt();
        int graph[]  = new int[quantity];
        int i = 0;
        int merge = 0;

        while (sc.hasNext()){
            int a = sc.nextInt();
            int b = sc.nextInt();

            if (graph[a - 1] == 0 && graph[b - 1] == 0){
                i++;
                graph[a - 1] = i;
                graph[b - 1] = i;
            }
            else if (graph[a - 1] != 0 && graph[b - 1] == 0){
                graph[b - 1] = graph[a - 1];
            }
            else if (graph[a - 1] == 0 && graph[b - 1] != 0){
                graph[a - 1] = graph[b - 1];
            }
            else if (graph[a - 1] != 0 && graph[b - 1] != 0){
                merge++;
                if (graph[a - 1] < graph[b - 1]){
                    int temp = graph[b - 1];
                    for (int k = 0; k < quantity; k++) {
                        if (graph[k] == temp){
                            graph[k] = graph[a - 1];
                        }
                    }
                }
                else {
                    for (int k = 0; k < quantity; k++){
                        int temp = graph[a - 1];
                        if (graph[k] == temp){
                            graph[k] = graph[b - 1];
                        }
                    }
                }
            }
        }
        for (int k = 0; k < quantity; k++) {
            if (graph[k] == 0)
                graph[k] = ++i;

        }
        System.out.println(Arrays.toString(graph));
        System.out.println("We need to add n edges in order for the graph to become connected: " + (i - merge - 1));
        System.out.println("So that we have forlabs again");
    }
}
