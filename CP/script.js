document.getElementById('vehicleForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const placa = document.getElementById('placa').value;
  const motorista = document.getElementById('motorista').value;
  const rota = document.getElementById('rota').value;
  const horarioSaida = document.getElementById('horarioSaida').value;
  const kmSaida = document.getElementById('kmSaida').value;

  // Criar objeto com dados do veículo
  const vehicleData = {
    placa: placa,
    motorista: motorista,
    rota: rota,
    horarioSaida: horarioSaida,
    kmSaida: kmSaida
  };
  

  // Armazenar dados localmente (pode ser substituído por envio para um servidor)
  localStorage.setItem('currentVehicle', JSON.stringify(vehicleData));

// Adicionar evento de clique no botão "Aberto"
document.getElementById('abertoBtn').addEventListener('click', function() {
  // Redirecionar para a página do Kanban
  window.location.href = 'kanban.html';
})})
