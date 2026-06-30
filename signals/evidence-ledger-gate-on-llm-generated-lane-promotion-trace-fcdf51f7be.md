# Evidence-ledger gate on LLM-generated lane-promotion traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gate-on-llm-generated-lane-promotion-trace-fcdf51f7be`
Run ID: `evidence-ledger-gate-on-llm-generated-lane-promotion-trace-fcdf51f7be-20260613T095500220961+0000`

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

- Parent run decision: Evidence-ledger agent reliability for lane promotion decisions: enoch://control-plane/projects/evidence-ledger-agent-reliability-for-lane-promotion-decisions-32a2a3832c09/runs/evidence-ledger-agent-reliability-for-lane-promotion-decisions-32a2a3832c09-20260613T093751979460+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bb53858795a

## What looked useful

The gate met its predefined Tier 1 threshold on 9 controlled traces: 3/3 valid promotions accepted, 6/6 unsupported promotions rejected, 0 false accepts, 0 false rejects.

## Boundaries and scale limits

Only 9 controlled hand-labeled traces; no live LLM sampling, no noisy parser, no large corpus, no integration with a real promotion controller.

## Claim scope

Tier 1 controlled small direct test of a deterministic evidence-ledger gate over 9 hand-labeled LLM-marked lane-promotion traces.

## Why it stopped

No-paper closure: Tier 1 controlled direct evidence supports the mechanism but is too small and controlled for publication-grade validation.

## Recommended next action

Run the bounded live-LLM deepen test before considering paper writing; this run is a useful Tier 1 mechanism signal only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM lane-promotion trace gate confirmation
- Success threshold: 0 false accepts and false_reject_rate <= 0.05 on at least 100 live LLM-generated traces.
- Stop condition: Stop if any unsupported promotion passes the strict gate or if false rejects exceed 5% after prompt/parser fixes documented before the run.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gate-on-llm-generated-lane-promotion-trace-fcdf51f7be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
