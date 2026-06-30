# Natural-Language Drafted Ledger Claims on Real Agent Trace Summaries

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-drafted-ledger-claims-on-real-agent-trace-495ac880a9`
Run ID: `natural-language-drafted-ledger-claims-on-real-agent-trace-495ac880a9-20260524T001212841572+0000`

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

- Parent run decision: Speculative Agent Verification via Draft-Verify Ledger: enoch://control-plane/projects/speculative-agent-verification-via-draft-verify-ledger-2191689b1909/runs/speculative-agent-verification-via-draft-verify-ledger-2191689b1909-20260523T215343991739+0000
- Parent run decision: Draft-Verify Ledger on Real LLM Tool-Agent Traces: enoch://control-plane/projects/draft-verify-ledger-on-real-llm-tool-agent-traces-1dfde503ad/runs/draft-verify-ledger-on-real-llm-tool-agent-traces-1dfde503ad-20260523T222413092588+0000

## What looked useful

Source-bound verification reached mean F1 1.000 across five fixed seeds, versus 0.598 lexical baseline, 0.682 summary-only ablation, and 0.749 global-unscoped ablation. Project scoping was necessary to reject borrowed cross-project evidence.

## Boundaries and scale limits

Claims were template-drafted and programmatically labeled from local Enoch artifacts; this does not validate independently authored free-form agent claims, human labels, open-ended semantic entailment, numeric table reasoning, adversarial paraphrase, or downstream decision quality.

## Claim scope

On 7,456 programmatically drafted natural-language claim cases from real Enoch run summaries across five fixed seeds, a source-bound project-local parser/verifier can classify support for decision, artifact, and command claims substantially better than lexical, summary-only, and globally unscoped baselines.

## Why it stopped

Tier 2 mechanism threshold was met, but the result remains template/programmatic-label evidence rather than publication-grade natural claim verification.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with independently authored natural claims and human or independent support labels over real agent trace summaries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-adjudicated natural claim verification on real agent trace summaries
- Success threshold: Source-bound semantic verifier F1 >= 0.85, at least +0.15 F1 over best baseline, supported-claim recall >= 0.85, and wrong-project false-positive rate <= 0.05 on held-out human-labeled claims.
- Stop condition: Stop if independent natural-claim F1 is below 0.70, if the best baseline is within 0.05 F1 of the source-bound verifier, or if wrong-project false-positive rate exceeds 0.10.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-drafted-ledger-claims-on-real-agent-trace-495ac880a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
