# Train 3 Medusa heads for zero-VRAM-draft on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `train-3-medusa-heads-for-zero-vram-draft-on-gpt-2-small-9230dc1570b7`
Run ID: `train-3-medusa-heads-for-zero-vram-draft-on-gpt-2-small-9230dc1570b7-20260527T135913850275+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/74f9f265566c

## What looked useful

After 800 steps, offset +2 top-1 improved from 0.0221 baseline to 0.1192 and top-10 from 0.1477 to 0.3559; offset +3 top-1 improved from 0.0202 to 0.0606 and top-10 from 0.0969 to 0.2699. A timing probe measured one GPT-2 forward plus three heads at 1.48x one base forward and 2.87x cheaper than four naive sequential base forwards without KV cache.

## Boundaries and scale limits

800 optimizer steps on Wikitext-2 validation only; no full Medusa tree verification, no KV-cache decode benchmark, no generation quality evaluation, no checkpoint persistence/reload test, one seed, and the heads add 115,792,128 parameters (~220.9 MiB bf16), so the result is not literally zero additional VRAM.

## Claim scope

Bounded local GPT-2-small/Wikitext-2 probe: three frozen-backbone Medusa-style heads can be trained quickly and learn measurable +1/+2/+3 future-token prediction signals without a separate draft backbone.

## Why it stopped

This run produced a useful local mechanism signal but only proxy prediction and proposal-overhead evidence, not direct decode-speed validation or paper-grade robustness.

## Recommended next action

Run a bounded decode-time follow-up that saves/reloads the trained heads and measures Medusa tree acceptance, accepted tokens per base forward, and end-to-end tokens/s versus a GPT-2-small KV-cache autoregressive baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Decode-time Medusa acceptance benchmark for GPT-2-small heads
- Success threshold: At least 1.3x end-to-end tokens/s improvement over KV-cache autoregressive GPT-2-small on a fixed prompt suite, with accepted tokens per base forward above 1.2 and no worse than 2% relative degradation on the chosen quality/perplexity guardrail.
- Stop condition: Stop if accepted tokens per base forward is <=1.05 or end-to-end decoding is not faster than the KV-cache baseline after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/train-3-medusa-heads-for-zero-vram-draft-on-gpt-2-small-9230dc1570b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
