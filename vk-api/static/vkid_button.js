const VKID = window.VKIDSDK;


VKID.Config.set({
  app: 51945044, // Идентификатор приложения.
  redirectUrl: "https://aide.zapto.org/auth_success", // Адрес для перехода после авторизации.
  state: 'feel-good' // Произвольная строка состояния приложения.
});

// Создание экземпляра кнопки.
const oneTap = new VKID.OneTap();

// Получение контейнера из разметки.
const container = document.getElementById('VkIdSdkOneTap');

// Проверка наличия кнопки в разметке.
if (container) {
  // Отрисовка кнопки в контейнере с именем приложения APP_NAME, светлой темой и на русском языке.
  oneTap.render({ container: container, scheme: VKID.Scheme.LIGHT, lang: VKID.Languages.RUS });
}

