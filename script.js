// وظائف الأزرار
function startGame() {
  alert("تم بدء اللعبة!");
  // أضف منطق بدء اللعبة هنا
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

// إنشاء فقاعات العملات الرقمية ديناميكيًا
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
  // عرض اسم العملة مع قوة العملة
  bubble.textContent = `${currency.name} (${currency.strength})`;
  
  // تعيين موضع عشوائي داخل الشاشة
  const topPos = Math.random() * 80 + 10; // من 10% إلى 90%
  const leftPos = Math.random() * 80 + 10;
  bubble.style.top = `${topPos}%`;
  bubble.style.left = `${leftPos}%`;
  
  // تحديد حجم الفقاعة بناءً على قوة العملة
  let size = 80; // الحجم الافتراضي
  if (currency.strength === "High") {
    size = 100;
  } else if (currency.strength === "Low") {
    size = 60;
  }
  bubble.style.width = `${size}px`;
  bubble.style.height = `${size}px`;
  bubble.style.lineHeight = `${size}px`; // لتوسيط النص عموديًا
  
  bubblesContainer.appendChild(bubble);
});