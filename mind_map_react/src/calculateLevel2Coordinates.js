export default function calculateLevel2Coordinates({
  numberOfNodes,
  parent,
  radius,
  index
}) {
  const slice = Math.PI / (numberOfNodes - 1);
  const angle = slice * index + parent.angle - (90 * Math.PI) / 180;
  const x = parent.x + radius * Math.cos(angle);
  const y = parent.y + radius * Math.sin(angle);
  return { x, y, angle };
}
