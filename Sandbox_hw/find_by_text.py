text = driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
print(f'The text {text} shown in the page ')

text1 = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
print(f'The text {text1} shown in the page ')


text = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
print(f'The text {text} shown in the page ')

#By class
text1 = driver.find_element(By.CSS_SELECTOR, "div[class*='styles__AlertDisplayStyles-sc-vw2fsn-0 gieqYR']").text
print(f'The text {text1} shown in the page by class ')