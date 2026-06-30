# 20M Draft Speculative Decoding for GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `20m-draft-speculative-decoding-for-gpt-2-small-2f0ab7c38268`
Run ID: `20m-draft-speculative-decoding-for-gpt-2-small-2f0ab7c38268-20260531T200821833837+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8d9c62e110b1

## What looked useful

Architecture size alone is not enough: the 19.4M random draft had 0.65% greedy next-token agreement and 0.272x target throughput. A much larger pretrained distilgpt2 assistant had 78.65% agreement but still only 0.552x target throughput in the main run and at best about 0.60x in a lookahead sweep.

## Boundaries and scale limits

Only 12 fixed prompts and 768 generated tokens in the main benchmark, plus a 6-prompt distilgpt2 lookahead sweep. No trained 20M draft checkpoint was available; the 20M-scale assistant was random and serves only as a mechanics/negative-control probe.

## Claim scope

On NVIDIA GB10 with Hugging Face assisted generation, GPT-2-small greedy decoding outperformed the tested small assistants: a 19.4M random GPT-2-style draft, sshleifer/tiny-gpt2, and distilgpt2. The result is a no-paper local benchmark and negative control, not a full validation of a trained 20M distilled draft.

## Why it stopped

Proxy/early falsification rather than full validation: tested small/off-the-shelf and random 20M-scale assistants were slower than greedy GPT-2-small, and no trained 20M draft was available to close the exact hypothesis.

## Recommended next action

Stop this run as a proxy/early negative result; the only worthwhile next bounded test is to train or distill a real approximately 20M GPT-2-tokenizer draft and require at least 1.15x greedy GPT-2-small throughput with exact greedy-output preservation over 1,000+ generated tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train and benchmark a distilled 20M GPT-2 draft for GPT-2-small speculative decoding
- Success threshold: At least 1.15x GPT-2-small greedy throughput on the same GB10 host while preserving exact deterministic target outputs and showing materially higher agreement per unit cost than distilgpt2.
- Stop condition: Stop as negative if the trained 20M draft is below 90% greedy next-token agreement or below 1.0x target greedy throughput after reasonable lookahead tuning.

## Evidence references

- Artifact root: `<local-path>/projects/20m-draft-speculative-decoding-for-gpt-2-small-2f0ab7c38268`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
