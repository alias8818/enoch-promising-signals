# Anchor-preserving KV compression with exact state reuse

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-preserving-kv-compression-with-exact-state-reuse-387bf0e4d598`
Run ID: `anchor-preserving-kv-compression-with-exact-state-reuse-387bf0e4d598-20260621T185001440024+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9fb28cddb478

## What looked useful

Exact anchor preservation consistently reduced mean KL by about 57-67% at 256 tokens and 59-65% at 512 tokens versus recent-only; anchor+pooled-middle reduced mean KL by about 53-77% at 256 tokens and 58-80% at 512 tokens, with paired wins over recent-only in nearly all samples.

## Boundaries and scale limits

Single GPT-2 model, WikiText-2 only, next-token logits only, no multi-token generation, no downstream long-context task accuracy, no real serving throughput benchmark, no RoPE model, and no implemented H2O/SnapKV/PyramidKV baseline comparison.

## Claim scope

On GPT-2 with WikiText-2 256-token and 512-token windows, preserving exact prefix anchor KV states plus recent KV states reduces next-token logit distribution drift versus a same-slot recent-only cache; simple pooled middle KV helps at larger budgets but is not uniformly better at the smallest budgets.

## Why it stopped

Closed as a no-paper useful signal: the local probe supports the mechanism but lacks direct downstream, serving, modern-model, and strong-baseline evidence required for publication.

## Recommended next action

Run a bounded deepen follow-up on a RoPE model with multi-token decoding and matched StreamingLLM/H2O/SnapKV-style baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-preserving KV compression on RoPE multi-token decoding with matched baselines
- Success threshold: At two or more memory budgets, anchor-preserving compression reduces multi-token KL by at least 25% versus recent-only and matches or beats a simple StreamingLLM/H2O-style baseline on generated-token agreement without worse memory accounting.
- Stop condition: Stop if anchor-preserving compression fails to beat recent-only on multi-token KL at matched budget, or if position/cache handling on a RoPE model requires recomputation that removes the exact-state reuse advantage.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-kv-compression-with-exact-state-reuse-387bf0e4d598`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
