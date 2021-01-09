package com.company;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.net.HttpURLConnection;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

/*
Создать консольное приложение для перевода текста
Запросить у пользователя имя файла и направление перевода
Обратиться к API переводчика, сделать запрос методом POST
Полученный ответ десереализовать из JSON в объект,
Вывести результат перевода и статус запроса (успешно или нет)
Справочник по API https://docs.microsoft.com/ru-ru/azure/cognitive-services/translator/reference/v3-0-reference
*/

class Translation {
    Translation(String text){
        this.text = text;
    }
    public String text;
}

class ServerResponse {
    public Translation[] translations;
}

public class Main {

    public static void main(String[] args) throws IOException {

        Gson gson = new Gson();

        Scanner in = new Scanner(System.in);

        System.out.println("Select the language to translate the text into: ");
        String LANGUAGE = in.nextLine();
        String API_URL = "https://api.cognitive.microsofttranslator.com/translate//?api-version=3.0&to=" + LANGUAGE;

        System.out.println("Enter the path to the file with text: ");
        String PATH = in.nextLine();
        String FILENAME = PATH.split("\\.")[0];

        try {
            FileInputStream stream = new FileInputStream(PATH);
            in = new Scanner(stream);

        } catch (IOException e){
            System.out.println("File not found.");
            return;
        }

        ArrayList<Translation> textToTranslate = new ArrayList<>();
        while (in.hasNext()){
            String line = in.nextLine();
            textToTranslate.add(new Translation(line));
        }

        in.close();


        String POSTData = gson.toJson(textToTranslate);

        URL url = new URL(API_URL);
        HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
        urlConnection.setRequestMethod("POST");
        urlConnection.addRequestProperty("Ocp-Apim-Subscription-Key", "b30b07d776cc433b94e9e3f3d57978de");
        urlConnection.addRequestProperty("Ocp-Apim-Subscription-Region", "westeurope");
        urlConnection.addRequestProperty("Content-Type", "application/json");
        urlConnection.setConnectTimeout(5000);
        urlConnection.setReadTimeout(5000);

        urlConnection.setDoOutput(true); //POST method
        OutputStream out = urlConnection.getOutputStream();
        out.write(POSTData.getBytes());
        out.close();


        Date date = new Date();
        SimpleDateFormat formatDate = new SimpleDateFormat("yyyy-MM-dd_hh-mm-ss");
        String newFileName = FILENAME + "_translated_" + LANGUAGE + "_" + formatDate.format(date) + ".txt";
        FileWriter writer = new FileWriter(newFileName);

        Type listType = new TypeToken<ArrayList<ServerResponse>>(){}.getType();
        ArrayList<ServerResponse> responses = new ArrayList<>();
        try {
            InputStreamReader reader = new InputStreamReader(urlConnection.getInputStream());
            responses = gson.fromJson(reader, listType);
            reader.close();
        } catch (IOException e){
            System.out.println(e);
            System.out.println("You entered incorrect language for translation...");
            return;
        }

        for (ServerResponse response: responses){
            for (Translation translation: response.translations){
                writer.write(translation.text);
            }
            writer.append('\n');
        }
        System.out.println("Translation completed successfully! It is in the file " + newFileName);
        urlConnection.disconnect();
        writer.close();
    }
}
