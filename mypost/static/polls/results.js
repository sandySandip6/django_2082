window.addEventListener('DOMContentLoaded', () => {
    const bars = document.querySelectorAll('.bar');
  
    bars.forEach(bar => {
      const votes = parseInt(bar.dataset.votes);
      const total = parseInt(bar.dataset.total);
      const percent = total > 0 ? (votes / total) * 100 : 0;
  
      bar.style.width = '0%';
      setTimeout(() => {
        bar.style.width = `${percent.toFixed(2)}%`;
      }, 100);
    });
  });
  