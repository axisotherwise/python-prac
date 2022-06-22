const $logoutBtn = document.querySelector("button");

$logoutBtn.addEventListener("click", e => {
  fetch("/logout")
    .then(() => location.href = "/")
    .catch(err => console.error(err));
});