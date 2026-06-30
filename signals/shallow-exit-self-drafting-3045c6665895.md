# Shallow-Exit Self-Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `shallow-exit-self-drafting-3045c6665895`
Run ID: `shallow-exit-self-drafting-3045c6665895-20260529T084813363680+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c0c56bfae25

## What looked useful

Early exits were cheap but inaccurate, while late exits were more accurate but too close to full-model cost. The best full-model top-1 match was 38.93% at layer 10/12, and every tested layer/draft-length combination stayed below 1x optimistic speedup.

## Boundaries and scale limits

Single small pretrained model, one validation corpus, offline one-token agreement plus analytic speed model; no trained early-exit heads, no 7B+ model, and no measured end-to-end speculative decoder latency.

## Claim scope

On GPT-2-small/WikiText-2 validation, untrained shallow exits using the pretrained hidden state, final layer norm, and tied LM head do not match full-model greedy next-token choices often enough to make shallow-exit self-drafting faster under an optimistic speculative decoding cost model.

## Why it stopped

Proxy/direct-small evidence falsified the simplest shallow-exit self-drafting mechanism: on 36,480 GPT-2-small token positions, acceptance was too low for speedup even before implementation overhead.

## Recommended next action

Stop this untrained/tied-head variant as a proxy early falsification; if continuing, run the bounded trained-exit-head follow-up before any larger-scale serving experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train lightweight shallow-exit heads for self-drafting
- Success threshold: Layer <= 6 exit achieves measured >1.1x end-to-end decoding throughput with identical greedy outputs on at least 1,000 prompts, not just analytic speedup.
- Stop condition: Stop if trained layer <= 6 exits cannot exceed 60% full-model greedy agreement or if measured speculative decoding throughput remains <=1.0x after implementation overhead.

## Evidence references

- Artifact root: `<local-path>/projects/shallow-exit-self-drafting-3045c6665895`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
