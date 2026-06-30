# Real Attention Trace Replay for Entropy-Spike KV Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-attention-trace-replay-for-entropy-spike-kv-selection-891bddc27d`
Run ID: `real-attention-trace-replay-for-entropy-spike-kv-selection-891bddc27d-20260523T022032765895+0000`

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

- Parent run decision: Entropy-Spike KV Selection for Long Context: enoch://control-plane/projects/entropy-spike-kv-selection-for-long-context-9556c4ed0b16/runs/entropy-spike-kv-selection-for-long-context-9556c4ed0b16-20260523T021604379178+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

Entropy-derived token scores are not useless: at 25% retained KV, windowed entropy-spike selection beats recency/random on distilgpt2 and gpt2 trace replay. However, the proposed windowed spike policy is dominated by even-stride and no-window high-entropy controls, and tight-budget behavior is weak.

## Boundaries and scale limits

Small CPU-only replay: 12 short texts for distilgpt2, 6 short texts for gpt2, max context 128, 473 non-smoke query evaluations. It does not test physical KV eviction during decoding, generation quality, serving latency, long contexts, or larger model families.

## Claim scope

Controlled small direct trace replay on GPT-2-family pretrained models shows windowed entropy-spike KV selection has some future-attention signal versus random/recency at 25% budget, but is not competitive with even-stride or direct high-entropy controls and fails against recency at 10% budget on distilgpt2.

## Why it stopped

No-paper useful signal from a controlled small direct test: mechanism support is mixed and the proposed windowed entropy-spike selection is beaten by simple controls, so the evidence is insufficient for publication readiness.

## Recommended next action

Stop this paper path; if continuing, test a bounded hybrid policy that combines high-entropy token selection with explicit early-anchor/stride retention in real truncated-KV decoding.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Hybrid Entropy-Anchor KV Selection Under Real Truncated Decoding
- Success threshold: Hybrid entropy-anchor policy improves retained-quality metric or token NLL by at least 5% relative to the best simple baseline at the same KV budget, with 95% paired bootstrap CI excluding zero on at least two model/text settings.
- Stop condition: Stop if the hybrid policy fails to beat the best of even-stride/anchor or high-entropy-only in the first two model/text settings, or if metadata overhead erases the effective KV budget advantage.

## Evidence references

- Artifact root: `<local-path>/projects/real-attention-trace-replay-for-entropy-spike-kv-selection-891bddc27d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
