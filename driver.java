package dev.selenium.hello;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class driver {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:\\driver\\chrome.exe");

    
        WebDriver driver = new ChromeDriver();

        driver.get("https://selenium.dev");

        driver.quit();
    }