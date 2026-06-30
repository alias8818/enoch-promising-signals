# Corpus-scale route persistence and heuristic baseline check for GPT-2 INT4/FP8 gating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `corpus-scale-route-persistence-and-heuristic-baseline-chec-a46fb8b814`
Run ID: `corpus-scale-route-persistence-and-heuristic-baseline-chec-a46fb8b814-20260629T013545119919+0000`

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

- Parent run decision: Per-Layer Learned INT4/FP8 Router with Reconstruction-Constrained Gate: enoch://control-plane/projects/per-layer-learned-int4-fp8-router-with-reconstruction-constrained-gate-a444c1698978/runs/per-layer-learned-int4-fp8-router-with-reconstruction-constrained-gate-a444c1698978-20260629T004723742914+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/640fda8882d3

## What looked useful

Adjacent route Jaccard was 0.23135 versus 0.00524 random expected, but global top-frequency baseline was 0.25268 and beat adjacent reuse in 10/12 layers. Simulated FP8 route Jaccard was 0.93588, while naive INT4 route Jaccard was 0.63490.

## Boundaries and scale limits

One pretrained GPT-2-small model, Wikitext-2 test split only, 280704 tokens, top-32 MLP post-activation routes, simulated activation quantization only; no gated inference kernels, quality/perplexity evaluation, training adaptation, larger GPT-2 variants, or 7B+ validation.

## Claim scope

Pretrained GPT-2-small MLP top-32 activation routes on the Wikitext-2 test split show strong adjacent-token persistence versus random, high simulated FP8 route agreement, moderate simulated INT4 route agreement, and weak support for previous-token route reuse as a standalone heuristic because a global top-frequency route baseline is better on macro average.

## Why it stopped

Proxy corpus evidence is mixed and specifically weakens the simple previous-token INT4/FP8 gating heuristic; it is not a full validation of gated inference or quantized serving.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded next test should implement actual routed GPT-2 MLP inference and compare quality/latency for FP8-stable routes against dense inference and train-split frequency baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual GPT-2 MLP routed-inference check for FP8-stable route subsets
- Success threshold: On Wikitext-2, routed inference achieves at least 20 percent measured MLP compute reduction with perplexity degradation under 5 percent relative to dense GPT-2-small, and beats previous-token and global-frequency heuristics on route recall or quality/latency Pareto.
- Stop condition: Stop if routed inference loses more than 10 percent relative perplexity at under 20 percent compute reduction or fails to beat the train-split frequency baseline.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-scale-route-persistence-and-heuristic-baseline-chec-a46fb8b814`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
