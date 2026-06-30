# Exact-Anchor KV Compression for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-cpu-inference-07c57df05b6a`
Run ID: `exact-anchor-kv-compression-for-cpu-inference-07c57df05b6a-20260614T023829746869+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ab1c977a3cf5

## What looked useful

Exact anchor rows plus grouped non-anchor summaries produced an 8.00x KV memory reduction and up to 7.04x speedup in the anchor-biased 8192-token proxy with about 0.097 relative L2 output error, but failed when attention was diffuse or when a salient non-anchor token was missed. Exact anchoring alone is not a correctness guarantee.

## Boundaries and scale limits

No real transformer model, no perplexity or downstream task metric, no production CPU kernel, no multi-layer decode loop, and no learned or online anchor-selection policy. Results are not a full validation of LLM CPU inference.

## Claim scope

Synthetic CPU single-token attention proxy for exact-anchor KV compression with fixed stride anchors and mean-compressed non-anchor groups, tested at sequence lengths 512 through 8192 and dimension 64.

## Why it stopped

Closed as a proxy useful-signal result, not full validation: synthetic evidence shows speed and memory promise but an explicit missed-token failure mode prevents a paper-positive claim.

## Recommended next action

Run a bounded real-model follow-up using a small autoregressive model with online anchor promotion, comparing full KV against exact-anchor compression on decode latency and perplexity or next-token KL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online Anchor Promotion for Exact-Anchor KV Compression in Small CPU Decode
- Success threshold: At least 4x KV memory reduction with at least 2x single-token decode attention speedup and mean next-token KL below 0.02 versus full KV on a bounded real-prompt suite, with no missed high-attention token above 0.10 attention mass.
- Stop condition: Stop if online promotion cannot keep next-token KL below 0.05 at 4x KV reduction or if CPU latency improvement falls below 1.5x after accounting for promotion overhead.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-cpu-inference-07c57df05b6a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
