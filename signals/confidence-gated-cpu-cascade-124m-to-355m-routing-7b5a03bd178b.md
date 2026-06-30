# Confidence-Gated CPU Cascade: 124M to 355M Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `68`
Project ID: `confidence-gated-cpu-cascade-124m-to-355m-routing-7b5a03bd178b`
Run ID: `confidence-gated-cpu-cascade-124m-to-355m-routing-7b5a03bd178b-20260609T161322677865+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e71c81d1a98c

## What looked useful

On the bounded proxy, GPT-2 small scored 81.25% accuracy at 0.571 s/example, the larger cached fallback scored 93.75% at 2.818 s/example, and the best cascade threshold tested reached 93.75% at 1.482 s/example, 52.6% of always-large latency. The small model's mistakes were low confidence, so confidence gating recovered most large-model benefit on this toy set.

## Boundaries and scale limits

This did not use the exact requested GPT-2-medium 355M fallback because it was not available in the local cache and prior Hugging Face download paths stalled. It did not use HellaSwag or another external benchmark because dataset download stalled. The dataset is tiny, hand-built, factual, and not representative of production routing or broad language modeling.

## Claim scope

Bounded CPU proxy on 16 built-in factual cloze multiple-choice items using cached GPT-2 124M as the router and cached Qwen2.5-0.5B-Instruct as the larger fallback. A confidence threshold around 0.40 matched always-large accuracy while escalating 31.25% of examples.

## Why it stopped

Proxy-only bounded result: useful mechanism evidence but not full 124M-to-355M validation and not publication-grade.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should rerun the same script on cached/downloaded GPT-2-medium 355M and a real multiple-choice benchmark such as HellaSwag with at least several hundred examples.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2 124M to GPT-2-medium 355M Cascade on HellaSwag
- Success threshold: A cascade threshold achieves >=80% of the large-minus-small accuracy gain with <=60% of always-large mean latency and no more than 1 percentage point absolute accuracy loss versus always-large.
- Stop condition: Stop as negative if GPT-2 confidence is poorly ordered, if the cascade needs >75% escalation to approach large-model accuracy, or if exact model/data downloads cannot be completed within the bounded run budget.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cpu-cascade-124m-to-355m-routing-7b5a03bd178b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
