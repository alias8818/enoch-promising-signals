# Residual cascade on real tool-call router traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-cascade-on-real-tool-call-router-traces-071344e76f`
Run ID: `residual-cascade-on-real-tool-call-router-traces-071344e76f-20260526T235211775405+0000`

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

- Parent run decision: Residual cascade for 3-bit home tool-use agents: enoch://control-plane/projects/residual-cascade-for-3-bit-home-tool-use-agents-cbadaf31c0b5/runs/residual-cascade-for-3-bit-home-tool-use-agents-cbadaf31c0b5-20260524T212401008938+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3865595438b

## What looked useful

Residual repair exists: the primary split improved accuracy by +6.57 points with 7.14% residual invocation and 2.31% proxy cost overhead. But hallucination/error reduction was only 16.55% and external bloat was +7.14 points, missing the required >=20% error reduction and <=5 point bloat caps. Across 5 seeds at the 5% train bloat cap, no run passed; mean error reduction was 10.62%.

## Boundaries and scale limits

Single cached trace corpus, 350-row held-out splits, deterministic replay rather than live serving, proxy cost model, and no separate stronger-model escalation trace.

## Claim scope

On a cached 1,000-row real local-LLM SQuAD/GSM8K direct/retrieve/tool trace dataset, a simple residual second-stage router improves held-out accuracy over a base router but does not satisfy the combined error-reduction and external-call budget threshold.

## Why it stopped

Direct Tier-1 replay on real cached tool/router traces falsified the stated success threshold for the simple residual cascade: useful accuracy gains required too much external-call bloat and did not reach the error-reduction target.

## Recommended next action

Stop this branch as no-paper useful evidence; a future bounded deepen should replace the hand-built residual score with a calibrated learned residual risk/action model and add true stronger-model escalation traces before reconsidering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated learned residual gate with true escalation traces
- Success threshold: Across at least 5 held-out split seeds, mean accuracy gain >=3 points, mean error reduction >=20%, residual invocation <=50%, external action bloat <=5 points, and measured/proxy latency overhead <=8%, with no split violating bloat by more than 1 point.
- Stop condition: Stop if the calibrated learned gate cannot beat the hand-built residual score on mean error reduction while staying within the external-call budget, or if stronger-model traces show escalation does not repair enough residual failures to justify the added path.

## Evidence references

- Artifact root: `<local-path>/projects/residual-cascade-on-real-tool-call-router-traces-071344e76f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
