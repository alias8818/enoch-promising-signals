# Validate structured evidence ledgers on real tiny LLM/tool-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `validate-structured-evidence-ledgers-on-real-tiny-llm-tool-b3c63fc7af`
Run ID: `validate-structured-evidence-ledgers-on-real-tiny-llm-tool-b3c63fc7af-20260531T135954265250+0000`

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

- Parent run decision: Structured evidence ledger for tiny agent tool reliability: enoch://control-plane/projects/structured-evidence-ledger-for-tiny-agent-tool-reliability-0a00fd61f864/runs/structured-evidence-ledger-for-tiny-agent-tool-reliability-0a00fd61f864-20260530T034943513104+0000
- Parent run decision: Real tiny-agent trace validation of structured evidence ledgers: enoch://control-plane/projects/real-tiny-agent-trace-validation-of-structured-evidence-le-3c7035a466/runs/real-tiny-agent-trace-validation-of-structured-evidence-le-3c7035a466-20260530T085223476385+0000

## What looked useful

Structured support links plus recomputed tool-validity features reached 0.933 accuracy and 0.972 AUROC versus 0.571 accuracy and 0.574 AUROC for the transcript baseline; paired bootstrap accuracy delta versus the best non-full ablation was +0.143 with 95% CI [0.100, 0.192].

## Boundaries and scale limits

The agent policy and error distribution were scaffolded; the tiny LM did not autonomously choose tools. The task domain was arithmetic only, with three seeds and one tiny pretrained model. No production, human, web/API, or larger instruction-tuned agent traces were tested.

## Claim scope

On 240 fixed-seed arithmetic calculator tool-agent traces containing real sshleifer/tiny-gpt2 sampled assistant text, structured evidence ledger features improved post-hoc final-answer correctness detection over final-text and transcript TF-IDF baselines and over ledger ablations.

## Why it stopped

Useful mechanism support on controlled real tiny-LM trace text, but not a publication-grade validation because the tool-agent decisions and failure mixture were scaffolded.

## Recommended next action

Stop paper escalation for this run; run a bounded deepen follow-up using an instruction-tuned small model that autonomously chooses calculator and lookup tools under the same ledger audit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autonomous small-instruction-model ledger audit on mixed calculator and lookup tools
- Success threshold: Full structured ledger accuracy exceeds the best non-full baseline by at least 0.10 with a paired bootstrap 95% CI lower bound above 0.03, and AUROC improves by at least 0.10.
- Stop condition: Stop if the autonomous model fails to produce parseable tool traces on at least 70% of tasks or if the full ledger advantage over the best baseline is below 0.03 accuracy after 300 traces.

## Evidence references

- Artifact root: `<local-path>/projects/validate-structured-evidence-ledgers-on-real-tiny-llm-tool-b3c63fc7af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
