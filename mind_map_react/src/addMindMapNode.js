import React from 'react';
import MindMapNode from './MindMapNode';
import renderToSprite from './renderToSprite';

const width = 120;
const height = 60;

export default async function addMindMapNode(scene, { level, label, x, y }) {
  const mindMapNode = await renderToSprite(
    <MindMapNode level={level} label={label} />,
    {
      width,
      height
    }
  );
  mindMapNode.scale.set(width / 100, height / 100, 0.1);
  mindMapNode.position.set(x, y);
  scene.add(mindMapNode);
}
