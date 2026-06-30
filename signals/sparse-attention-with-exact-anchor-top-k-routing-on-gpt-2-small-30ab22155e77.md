# Sparse attention with exact-anchor top-k routing on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-attention-with-exact-anchor-top-k-routing-on-gpt-2-small-30ab22155e77`
Run ID: `sparse-attention-with-exact-anchor-top-k-routing-on-gpt-2-small-30ab22155e77-20260609T225310113178+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b997fa0ab8

## What looked useful

Exact-anchor top-k routing is easy to evaluate as a deterministic mask, but when applied post-hoc to GPT-2-small it trades quality sharply for edge reduction. The best aggressive 256-token setting tested used 42.5% edges and raised perplexity from 39.74 to 48.15; a 512-token permissive setting reached perplexity 32.44 vs dense 31.62 but used 73.7% edges.

## Boundaries and scale limits

No sparse CUDA kernel was implemented; runtime is not evidence for speed. No training or fine-tuning under the sparse mask was run. Evaluation used WikiText-2 validation subsets, not broad downstream or long-context benchmarks.

## Claim scope

Post-hoc exact-anchor top-k routed attention masks on pretrained GPT-2-small were evaluated on WikiText-2 validation at 256-token and 512-token sequence lengths. Aggressive masks at roughly 22% to 48% of dense causal edges caused material perplexity degradation; near-baseline quality required a permissive mask using about 74% of dense edges.

## Why it stopped

Proxy/local early falsification of post-hoc quality preservation, not a full validation or final rejection of trained sparse-routing models.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should fine-tune GPT-2-small with the routed mask and require quality recovery at no more than 50% dense attention edges before revisiting kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fine-tune GPT-2-small with exact-anchor routed masks at <=50% dense edges
- Success threshold: Routed model validation perplexity within 5% of dense fine-tuned control while using <=50% dense causal attention edges.
- Stop condition: Stop if after the matched fine-tuning budget the best routed configuration remains >10% worse in perplexity than the dense control or needs >60% dense edges to recover quality.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-attention-with-exact-anchor-top-k-routing-on-gpt-2-small-30ab22155e77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
