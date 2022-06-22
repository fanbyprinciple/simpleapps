export default function calculateLevel1Coordinates({
  numberOfNodes,
  parent,
  radius,
  index
}) {
  const slice = (2 * Math.PI) / numberOfNodes;
  const angle = slice * index - Math.PI / 2;
  const x = parent.x + radius * Math.cos(angle);
  const y = parent.y + radius * Math.sin(angle);
  return { x, y, angle };
}
