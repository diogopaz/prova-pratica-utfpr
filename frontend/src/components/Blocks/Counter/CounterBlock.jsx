// src/components/Blocks/CounterBlock.jsx

import React, { useState } from 'react';

const CounterBlock = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  const reset = () => {
    setCount(0);
  };

  return (
    <div style={{padding: 10}}>
      <h2>Contador</h2>
      <div style={{fontSize: 52, padding: 20}}>{count}</div>
      <button onClick={increment} style={{margin: 5, padding: 3, borderRadius: 5}}>Incrementar</button>
      <button onClick={reset} style={{margin: 5, padding: 3, borderRadius: 5}}>Zerar</button>
    </div>
  );
};

export default CounterBlock;
