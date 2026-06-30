# Attention-Entropy KV Eviction for Long Context on CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `attention-entropy-kv-eviction-for-long-context-on-cpu-inference-aa8400a29ac0`
Run ID: `attention-entropy-kv-eviction-for-long-context-on-cpu-inference-aa8400a29ac0-20260609T045839861024+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4890047f9ba5

## What looked useful

Low-entropy eviction ranked near recency on retained mass and L2 output error but had 0.9686-0.9975 mean cache overlap with recency in the diagnostic, indicating the apparent win is mostly recency-equivalent. High-entropy and mass/entropy policies produced distinct cache sets but generally lost substantial attention mass and increased output error.

## Boundaries and scale limits

No real transformer perplexity, task accuracy, layer/head ablation, or CPU serving latency was measured. Sequence length was 1024 for the main simulator and 512 for the recency-overlap diagnostic, with synthetic attention regimes rather than model-derived traces.

## Claim scope

Bounded proxy evidence on synthetic online attention traces for CPU-oriented KV cache eviction: entropy-only policies do not provide a distinct useful eviction signal beyond recency, and entropy variants that diverge from recency hurt attention-mass retention and output reconstruction.

## Why it stopped

Proxy early falsification rather than full validation: the only entropy policy that preserved outputs was effectively recency, while distinct entropy-driven policies degraded output reconstruction.

## Recommended next action

Run one bounded real-model deepen test on a small CPU-runnable decoder with recency, low-entropy, and recent-plus-low-entropy KV eviction; stop unless entropy beats recency on quality while showing substantially lower cache overlap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small real-model KV eviction test for entropy-vs-recency separation
- Success threshold: Entropy-based eviction must improve quality by at least 2% relative to recency at one cache fraction without worse quality at the others, and its mean cache overlap with recency must be below 0.85.
- Stop condition: Stop if low-entropy remains recency-equivalent with overlap at or above 0.9, or if any quality gains are within noise while latency or bookkeeping overhead increases.

## Evidence references

- Artifact root: `<local-path>/projects/attention-entropy-kv-eviction-for-long-context-on-cpu-inference-aa8400a29ac0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
