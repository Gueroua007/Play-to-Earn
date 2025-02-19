// وظائف الأزرار
function startGame() {
  alert("تم بدء اللعبة!");
  // أضف منطق بدء اللعبة هنا.
}
function handleHome() {
  alert("الانتقال إلى الصفحة الرئيسية");
}
function handleTask() {
  alert("عرض المهام");
}
function handleReferral() {
  alert("دعوة الأصدقاء");
}
function handleWallet() {
  alert("عرض المحفظة");
}

// إنشاء فقاعات العملات الرقمية ودفعها للتحرك عشوائيًا
const currencies = [
  { name: "Bitcoin", strength: "High" },
  { name: "Ethereum", strength: "Medium" },
  { name: "Ripple", strength: "Low" },
  { name: "Litecoin", strength: "Medium" },
  { name: "Cardano", strength: "High" }
];

const bubblesContainer = document.querySelector('.bubbles-container');

currencies.forEach(currency => {
  const bubble = document.createElement('div');
  bubble.classList.add('bubble');
  bubble.textContent = `${currency.name} (${currency.strength})`;
  
  // تعيين موقع مبدئي عشوائي داخل الشاشة
  bubble.style.top = `${Math.random() * 100}%`;
  bubble.style.left = `${Math.random() * 100}%`;
  
  // تحديد حجم الفقاعة بناءً على قوة العملة
  let size = 80;
  if (currency.strength === "High") {
    size = 100;
  } else if (currency.strength === "Low") {
    size = 60;
  }
  bubble.style.width = `${size}px`;
  bubble.style.height = `${size}px`;
  bubble.style.lineHeight = `${size}px`; // لتوسيط النص عموديًا
  
  bubblesContainer.appendChild(bubble);
  
  // تحديث موقع الفقاعة بشكل عشوائي كل 5 ثوانٍ
  setInterval(() => {
    bubble.style.top = `${Math.random() * 100}%`;
    bubble.style.left = `${Math.random() * 100}%`;
  }, 5000);
});