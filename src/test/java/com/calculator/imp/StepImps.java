package com.calculator.imp;

import com.thoughtworks.gauge.Step;
import com.calculator.steps.BaseSteps;
import lombok.extern.log4j.Log4j;
import org.openqa.selenium.WebElement;

@Log4j
public class StepImps {
    private final BaseSteps baseSteps;
    private final LoggerImps loggerImps = LoggerImps.getInstance(log);
    public static int DEFAULT_SECOND_WAIT_AMOUNT = 20;

    public StepImps() {
        baseSteps = BaseSteps.getInstance();
    }

    @Step({"Elementine tikla <key>"})
    public void click(String keyword) {
        baseSteps.click(keyword);
    }

    @Step({"<text> textini <key> elemente yaz"})
    public void sendKeys(String text, String keyword) {
        baseSteps.sendKeys(keyword, text);
    }

    @Step({"<key> elementini kontrol et"})
    public void waitIfNotExist(String key) {
        baseSteps.waitIfNotExist(key);
    }

    @Step({"Elementinin yuklenmesini bekle <key>"})
    public void waitIfNotExistWithTime(String key) {
        baseSteps.waitIfNotExistWithTime(key, DEFAULT_SECOND_WAIT_AMOUNT);
    }

    @Step({"<int> saniye bekle"})
    public void waitBySeconds(int seconds) {
        try {
            Thread.sleep(seconds * 1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Step("<key> elementin ustunde bekle")
    public void hover(String key) {
        baseSteps.mouseHover(key);
    }

    @Step({"Su an ki URL <url> degerini iceriyor mu kontrol et"})
    public void checkURLContainsRepeat(String expectedURL) {
        baseSteps.checkUrl(expectedURL);
    }

    @Step({"<key> li elementi bul ve sonuc değerini <saveKey> olarak sakla"})
    public void saveNumericValueByKey(String key, String saveKey) throws InterruptedException {
        WebElement element;
        int waitVar = 0;
        element = baseSteps.findElement(key);
        while (true) {
            if (element.isDisplayed()) {
                String elementValue = element.getText().trim();
                String numericValue = elementValue.replace("=", "").trim();
                baseSteps.setValueToStorage(saveKey, numericValue);
                loggerImps.info(waitVar + ". saniyede WebElement bulundu.");
                loggerImps.info("'" + saveKey + "' olarak sayısal değer kaydedildi: " + numericValue);
                break;
            } else {
                waitVar++;
                Thread.sleep(1000);
                if (waitVar == 20) {
                    throw new NullPointerException(String.format("'%s' anahtarına sahip element bulunamadı.", key));
                }
            }
        }
    }

    @Step({"<saveKey> ile kaydedilen değer ile <expectedValue> değerini karşılaştır"})
    public void compareSavedValueWithInput(String key, String expectedValue) {
       String numericValue = baseSteps.getValueFromStorage(key);
        if (numericValue.equals(expectedValue)) {
            loggerImps.info("Kaydedilen değer, beklenen değer ile eşleşiyor: " + expectedValue);
        } else {
            loggerImps.errorAndFail("Kaydedilen değer (" + numericValue + "), beklenen değer (" + expectedValue + ") ile eşleşmiyor.");
        }
    }

}