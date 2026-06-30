# Quantized-draft speculative cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-draft-speculative-cascade-8bbde575b1c8`
Run ID: `quantized-draft-speculative-cascade-8bbde575b1c8-20260614T001341932919+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3b5be52bae7

## What looked useful

The cascade mechanism increased target acceptance from 0.515 for direct intermediate drafting to 0.535, and from 0.221 for direct cheap-q4 drafting, but the extra 247 intermediate verification calls dominated. Modeled throughput was 346.5 tokens/s for cascade versus 431.5 for direct cheap-q4 and 392.7 for direct intermediate.

## Boundaries and scale limits

Small GPT-2-family models, 8 prompts, 32 generated tokens per prompt, fake quantized weights rather than int4 kernels, Python/Hugging Face trace harness rather than production KV-cache serving.

## Claim scope

On a bounded GPT-2-family trace benchmark using a fake-4-bit tiny GPT-2 cheap draft, DistilGPT-2 intermediate draft, and GPT-2 target on GB10 CUDA, a two-stage cascade raised target acceptance but reduced modeled and harness throughput versus direct speculative baselines.

## Why it stopped

Early proxy falsification: the tested cascade improved acceptance but did not improve throughput, and the result is not a full validation of production quantized speculative serving.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test whether KV-cache reuse plus a real quantized draft kernel can reduce intermediate overhead enough to beat direct speculative baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware quantized speculative cascade overhead test
- Success threshold: Cascade measured throughput is at least 10% higher than both direct cheap-draft and direct intermediate-draft baselines while preserving target acceptance at or above the direct intermediate baseline.
- Stop condition: Stop if cache-aware or real-quantized cascade throughput remains below the best direct baseline, or if acceptance gains are under 5 percentage points while intermediate overhead remains above 20% of total modeled cost.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-draft-speculative-cascade-8bbde575b1c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
