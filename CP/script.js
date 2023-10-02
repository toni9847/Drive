document.getElementById('vehicleForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const placa = document.getElementById('placa').value;
    const motorista = document.getElementById('motorista').value;
    const rota = document.getElementById('rota').value;
    const horarioSaida = document.getElementById('horarioSaida').value;
    const horarioChegada = document.getElementById('horarioChegada').value;
    const kmSaida = document.getElementById('kmSaida').value;
    const kmChegada = document.getElementById('kmChegada').value;
  
    // Aqui você pode enviar os dados para o backend ou fazer o que for necessário com eles
  
    // Exemplo de exibição dos dados
    alert(`
      Placa do Veículo: ${placa}
      Motorista: ${motorista}
      Rota: ${rota}
      Horário de Saída: ${horarioSaida}
      Horário de Chegada: ${horarioChegada}
      Km de Saída: ${kmSaida}
      Km de Chegada: ${kmChegada}
    `);
  });
  