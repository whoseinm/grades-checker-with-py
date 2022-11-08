print("Salam, mən sizə ananız üçün hədiyyə seçməyə kömək edəcəyəm.")
name = input("Sizin adınız nədir?")
print(name, ", ananız nə ilə maraqlanır? (kulinariya, kitab oxumaq, əl işləri, digər)")
hobby = input()
if hobby == "kulinariya":
   print("Salat qabı və ya yeməyi süfrəyə vermək üçün boşqab hədiyyə edin.")
elif hobby == "kitab oxumaq":
   print("Ananızda olan kitablara baxın və o mövzuya aid kitabları hədiyyə edin.")
elif hobby == "əl işləri":
   print("Əl işləri üçün dəst hədiyyə edin.")
else:
   print("Ananızla birlikdə olan şəklinzi gözəl çərçivədə hədiyyə edin.")
print("Sonra mütləq ananızı qucaqlayın və onu çox sevdiyinizi söyləyin.")