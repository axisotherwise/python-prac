const $logoutBtn = document.querySelector(".logout");

$logoutBtn.addEventListener("click", e => {
  fetch("/logout", { method: "DELETE" })
    .then(() => location.href = "/")
    .catch(err => console.error(err));
});