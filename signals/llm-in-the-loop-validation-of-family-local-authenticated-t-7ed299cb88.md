# LLM-in-the-loop validation of family-local authenticated trap panels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `llm-in-the-loop-validation-of-family-local-authenticated-t-7ed299cb88`
Run ID: `llm-in-the-loop-validation-of-family-local-authenticated-t-7ed299cb88-20260612T105804501901+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Authenticated multi-agent full-family local trap panel: enoch://control-plane/projects/authenticated-multi-agent-full-family-local-trap-panel-e7da28ac73/runs/authenticated-multi-agent-full-family-local-trap-panel-e7da28ac73-20260612T105257258923+0000
- Parent run decision: Trace real coding agents on the local adversarial trap suite: enoch://control-plane/projects/trace-real-coding-agents-on-the-local-adversarial-trap-sui-1cf5bfb742/runs/trace-real-coding-agents-on-the-local-adversarial-trap-sui-1cf5bfb742-20260612T103705470968+0000

## What looked useful

Family-local binding of trap-panel tags to family id, panel id, nonce, and answer closed cross-family replay and family-claim swap failures missed by global-auth, random-trap, and no-auth baselines. However, a small real LLM judge had 0.777 accuracy and 0.330 false-reject rate, so the LLM-in-the-loop claim is not paper-ready.

## Boundaries and scale limits

Synthetic rule-generated panels only; one small LLM adjudication probe with google/flan-t5-small; no real task corpus, no production LLM judge, no human-authored family panels, and no adaptive model attacker.

## Claim scope

In a fixed-seed synthetic numeric panel benchmark with 32 families, 250000 panels per condition, and explicit replay/forgery/wrong-answer attack classes, family-local HMAC authentication plus semantic answer checking eliminated the tested invalid classes while preserving valid paraphrases.

## Why it stopped

No-paper useful signal: the auth mechanism is supported on direct synthetic tests, but the LLM-in-the-loop adjudication portion remains mixed and the evidence is not production- or paper-grade.

## Recommended next action

Stop paper escalation for this run; if continuing within the depth cap, run a bounded deepen test on a real panel corpus with at least two stronger LLM judges and calibrated prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus LLM adjudication for family-local authenticated trap panels
- Success threshold: At least 0.95 valid accept rate and at least 0.99 invalid detection rate on the real-corpus benchmark, with cross-family replay and family-claim swap pass rates below 0.01 for both LLM-judged and deterministic-baseline variants.
- Stop condition: Stop if both stronger LLM judges remain below 0.95 valid accept rate after prompt calibration, or if family-local authentication no longer beats the best admissible baseline by at least 0.10 absolute invalid-detection lift.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-validation-of-family-local-authenticated-t-7ed299cb88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
