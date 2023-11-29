document.addEventListener('DOMContentLoaded', function () {
  // Recuperar dados armazenados localmente
  const currentVehicle = JSON.parse(localStorage.getItem('currentVehicle'));

  if (currentVehicle) {
    // Criar um cartão para o veículo em trânsito
    const card = createCard(currentVehicle);

    // Adicionar o cartão à coluna "Aberto"
    document.getElementById('aberto').appendChild(card);

    // Adicionar evento de clique no cartão
    card.addEventListener('click', function() {
      // Redirecionar para a página principal para completar as informações
      window.location.href = 'index.html';
    });
  }
});

// Função para criar um cartão com os dados do veículo
function createCard(vehicleData) {
  const card = document.createElement('div');
  card.classList.add('card');

  card.innerHTML = `
    <h3>Informações do Veículo</h3>
    <p><strong>Placa:</strong> ${vehicleData.placa}</p>
    <p><strong>Motorista:</strong> ${vehicleData.motorista}</p>
    <p><strong>Rota:</strong> ${vehicleData.rota}</p>
    <p><strong>Horário de Saída:</strong> ${vehicleData.horarioSaida}</p>
    <p><strong>Km de Saída:</strong> ${vehicleData.kmSaida}</p>
  `;

  return card;
}
