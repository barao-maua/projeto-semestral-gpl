export function calcularTotal() {
    const dataIda = document.getElementById('data_ida').value;
    const dataVolta = document.getElementById('data_volta').value;

    if (dataIda && dataVolta) {
        const ida = new Date(dataIda);
        const volta = new Date(dataVolta);
        const diff = (volta - ida) / (1000 * 60 * 60 * 24);

        if (diff > 0) {
            const total = diff * 320;
            document.getElementById('resumoDatas').textContent = `Período: ${dataIda} a ${dataVolta} (${diff} noites)`;
            document.getElementById('total_reserva').textContent = `Total: R$ ${total.toFixed(2).replace('.', ',')}`;
        } else {
            document.getElementById('total_reserva').textContent = '';
            document.getElementById('resumoDatas').classList = "font-bold text-red-600"
            document.getElementById('resumoDatas').textContent = 'A data de volta deve ser após a data de ida!';
        }
    } else {
        document.getElementById('total_reserva').textContent = '';
        document.getElementById('resumoDatas').textContent = '';
    }
}